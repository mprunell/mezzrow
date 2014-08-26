from django.conf.urls import url, patterns
from oscar.apps.dashboard.reports.app import ReportsApplication as CoreReportsApplication
from .views import TicketDetailsView


class ReportsApplication(CoreReportsApplication):
    ticket_details_view = TicketDetailsView

    def get_urls(self):
        urls = [
            url(r'^ticket-details/(?P<pk>\d+)/$', self.ticket_details_view.as_view(), name='ticket_details'),
            url(r'^$', self.index_view.as_view(), name='reports-index'),
        ]
        return self.post_process_urls(patterns('', *urls))

application = ReportsApplication()
