#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzmin
# __date__ = 2022/1/6
import pdfkit
from django.template import loader
from pdf2docx import parse


def html2pdf(template_name, context):
    template_str = loader.render_to_string(template_name, context)
    # 需要安装软件 https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf
    pdf_data = pdfkit.from_string(template_str, None, options={"--encoding": "UTF-8"})
    return pdf_data


def html2doc(pdf_file, docx_file):
    # convert pdf to docx
    parse(pdf_file, docx_file)