# -*- coding: utf-8 -*-
import logging
from django.core.mail.message import EmailMultiAlternatives
from django.utils.log import AdminEmailHandler as shippedAdminEmailHandler

logger = logging.getLogger(__name__)

class AdminEmailHandler(shippedAdminEmailHandler):
  def emit(self, record):
    import traceback
    from django.views.debug import ExceptionReporter

    try:
      request = record.request
      subject = '%s (%s): %s' % (
        record.levelname,
        request.META.get('REMOTE_ADDR'),
        record.msg
        )
      request_repr = repr(request)
    except Exception:
      subject = '%s: %s' % (
        record.levelname,
        record.msg
        )
      request = None
      request_repr = "Request repr() unavailable"

    if record.exc_info:
      exc_info = record.exc_info
      stack_trace = '\n'.join(traceback.format_exception(*record.exc_info))
    else:
      exc_info = (None, record.msg, None)
      stack_trace = 'No stack trace available'

    message = "%s\n\n%s" % (stack_trace, request_repr)
    reporter = ExceptionReporter(request, is_email=True, *exc_info)
    html_message = self.include_html and reporter.get_traceback_html() or None
    #        mail_admins(subject, message, fail_silently=True,
    mail_admins(subject, message, html_message=html_message)

class EmailMultiAlternativesUsingSmtp(EmailMultiAlternatives):
  def get_connection(self, fail_silently=False):
    from django.conf import settings
    from django.core.mail import get_connection
    if not self.connection:
      self.connection = get_connection(backend=settings.EMAIL_BACKEND_ADM,
                                       fail_silently=fail_silently)
    return self.connection



## send admin mails with smtp, regardless of settings.EMAIL_BACKEND
def mail_admins(subject, message, fail_silently=False, connection=None,
                html_message=None):
  """Sends a message to the admins, as defined by the ADMINS setting."""
  from django.conf import settings
  logger.info(u"sending admin email '%s'" % subject)
  mail = EmailMultiAlternativesUsingSmtp(u'[Django] %s' % subject,
                                         message, settings.ADMIN_FROM_EMAIL, [admin[1] for admin in settings.ADMINS],
                                         connection=connection)
  if html_message:
    mail.attach_alternative(html_message, 'text/html')
  mail.send(fail_silently=fail_silently)
