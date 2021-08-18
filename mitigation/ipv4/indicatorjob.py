from intstreamsdk.job import IndicatorJob
from intstreamsdk.client import SyncClient
from intstreamsdk import resource, mitigate

class MitigateJob(mitigate.MitigateJob):
    def __init__(self, client_class, ):
        super(MitigateJob, self).__init__(client_class, mitigate.RESOURCE_IPV4)

    def do_mitigate(self, indicator):
        """
        TODO: EDIT This method; return True to mitigate indicator
        all column data will be updated when this script runs.
        :param indicator: dict indicator object
        :return:  bool
        """

        return True

if __name__ == "__main__":
    # set env variables:
    # JOB_USERNAME
    # JOB_PASSWORD
    # JOB_SERVER_URL - base server url

    # initialize job object     with SyncClient or AsyncClient
    demo = MitigateJob(SyncClient)
    # add any
    demo.run()
