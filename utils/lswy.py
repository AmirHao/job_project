"""
无忧 创建/更新 company
"""


def create(self, validated_data):
    content = deepcopy(validated_data)
    super_manage_data = validated_data.pop('super_staff')
    super_manage_data['is_super'] = True
    company_address_data = validated_data.pop('company_address_')
    company_address_data['is_default'] = True
    company2tax_agent_data = validated_data.pop('company2tax_agent_')
    try:
        with transaction.atomic():
            # todo hzm 报错 Object of type Decimal is not JSON serializable
            # event = create_event('company', EventCategoryEnum.create.name,
            #                      content, EventStatusEnum.processing.name,
            #                      self.context['request'].user.id)
            company = Company.objects.create(**validated_data)
            no = spawn_model_no(True, company.id)
            company.no = no
            company.save(update_fields=['no'])

            super_manage_data['company'] = company
            super_manage_s = StaffManageSerializer()
            super_manage_s.create(super_manage_data)

            company_address_data['company'] = company
            company_address_s = CompanyAddressRetrieveSerializer()
            company_address_s.create(company_address_data)

            company2tax_agent_data.pop('id', None)
            company2tax_agent_data['company'] = company
            company2tax_agent_s = Company2TaxAgentRetrieveSerializer()
            company2tax_agent_s.create(company2tax_agent_data)
            # event.status = EventStatusEnum.succeed.name
            # event.save(update_fields=['status'])
    except:  # noqa
        settings.LLS_LOGGING.error(traceback.format_exc())
        raise ValidationError('创建失败，请重新创建')
    return company


def update(self, instance, validated_data):
    # todo hzm 更新 company2tax_agent 待做修改记录
    super_manage_data = validated_data.pop('super_staff', None)
    company_address_data = validated_data.pop('company_address_', None)
    company2tax_agent_data = validated_data.pop('company2tax_agent_', None)
    super_manage_obj = instance.staff.filter(is_super=True).first()
    company_address_obj = instance.company_address.filter(is_default=True).first()
    company2tax_agent_obj = instance.company2tax_agent.filter(is_enable=True).first()
    content = {'before': [], 'after': []}
    update_fields = {}
    # 对比本次更新内容
    for obj, update_data, model in zip([instance, super_manage_obj, company_address_obj],
                                       [validated_data, super_manage_data, company_address_data],
                                       ['company', 'staff', 'companyaddress']):
        res = get_update_content(obj, update_data, model)
        content['before'].extend(res['before'])
        content['after'].extend(res['after'])
        update_fields[model] = res.pop(model, None)
    if not content['after']:
        # 未有字段修改
        return
    try:
        with transaction.atomic():
            # todo hzm 更新 company2tax_agent 待做修改记录
            # todo hzm 报错 Object of type Decimal is not JSON serializable
            # event = create_event('company', EventCategoryEnum.update.name,
            #                      content, EventStatusEnum.processing.name,
            #                      self.context['request'].user.id)
            instance = super().update(instance, validated_data)
            if super_manage_data and update_fields['staff']:
                # 更新超级管理员
                super_manage_s = StaffManageSerializer()
                super_manage_s.update(super_manage_obj, super_manage_data)
            if company_address_data and update_fields['companyaddress']:
                # 更新默认地址
                company_address_s = CompanyAddressRetrieveSerializer()
                company_address_s.update(company_address_obj, company_address_data)
            if company2tax_agent_data:
                # 更新 关联开票公司信息
                company2tax_agent_data['company'] = instance
                company2tax_agent_s = Company2TaxAgentRetrieveSerializer()
                company2tax_agent_s.update(company2tax_agent_obj, company2tax_agent_data)

                # 以下代码支持 一个company关联多个tax_agent
                # company2tax_agent_ids = []
                # for company2tax_agent in company2tax_agent_data:
                #     company2tax_agent['company'] = instance
                #     company2tax_agent_s = Company2TaxAgentRetrieveSerializer()
                #     c2t_a = Company2TaxAgent.objects.filter(company_id=instance.id,
                #                                             tax_agent_id=company2tax_agent['tax_agent_id']).first()
                #     if c2t_a:
                #         company2tax_agent_s.update(c2t_a, company2tax_agent)
                #         company2tax_agent_ids.append(c2t_a.id)
                #     else:
                #         res = company2tax_agent_s.create(company2tax_agent)
                #         company2tax_agent_ids.append(res.id)
                # # 取消之前关联的 开票公司
                # Company2TaxAgent.objects.filter(company_id=instance.id).exclude(
                #     id__in=company2tax_agent_ids).update(is_enable=False)
            # event.status = EventStatusEnum.succeed.name
            # event.save(update_fields=['status'])
    except:  # noqa
        settings.LLS_LOGGING.error(traceback.format_exc())
        raise ValidationError('修改失败，请重重试')
    else:
        return instance


"""
无忧 创建/更新 tax_agent
"""


def create(self, validated_data):
    try:
        content = deepcopy(validated_data)
        super_manage_data = validated_data.pop('super_staff')
        super_manage_data['is_super'] = True
        tax_config_data = validated_data.pop('tax_config_')
        with transaction.atomic():
            # event = create_event('tax_agent', EventCategoryEnum.create.name,
            #                      content, EventStatusEnum.processing.name,
            #                      self.context['request'].user.id)

            tax_agent = TaxAgent.objects.create(**validated_data)
            no = spawn_model_no(True, tax_agent.id)
            tax_agent.no = no
            tax_agent.save(update_fields=['no'])

            super_manage_data['tax_agent'] = tax_agent
            super_manage_s = StaffManageSerializer()
            super_manage_s.create(validated_data=super_manage_data)

            tax_config_data['tax_agent'] = tax_agent
            tax_config_s = TaxConfigRetrieveSerializer()
            tax_config_s.create(validated_data=tax_config_data)

    except:  # noqa
        settings.LLS_LOGGING.error(traceback.format_exc())
        raise ValidationError('创建失败，请重新创建')
    return tax_agent


def update(self, instance, validated_data):
    super_manage_data = validated_data.pop('super_manage', None)
    tax_config_data = validated_data.pop('tax_config', None)
    super_manage_obj = instance.staff.filter(is_super=True).first()
    tax_config_obj = instance.tax_config.first()
    content = {'before': [], 'after': []}
    update_fields = {}
    for obj, update_data, model in zip([instance, super_manage_obj, tax_config_obj],
                                       [validated_data, super_manage_data, tax_config_data],
                                       ['tax_agent', 'staff', 'tax_config']):
        res = get_update_content(obj, update_data, model)
        content['before'].extend(res['before'])
        content['after'].extend(res['after'])
        update_fields[model] = res.pop(model, None)
    if not (content['before'] and content['after']):
        # 未有字段修改
        return
    try:
        with transaction.atomic():
            # event = create_event('tax_agent', EventCategoryEnum.update.name,
            #                      content, EventStatusEnum.processing.name,
            #                      self.context['request'].user.id)

            instance = super().update(instance, validated_data)
            if super_manage_data and update_fields['staff']:
                # 更新超级管理员变更信息
                super_manage_obj = instance.staff.first()
                super_manage_s = StaffManageSerializer()
                super_manage_s.update(super_manage_obj, validated_data=super_manage_data)
            if tax_config_data and update_fields['tax_config']:
                # 更新开票配置信息
                tax_config_obj = instance.tax_config.first()
                tax_config_s = TaxConfigRetrieveSerializer()
                tax_config_s.update(tax_config_obj, validated_data=tax_config_data)
    except:  # noqa
        settings.LLS_LOGGING.error([traceback.format_exc()])
        raise ValidationError('修改失败，请重重试')
    else:
        return instance
