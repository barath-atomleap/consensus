from homi import App, Server
from homi.extend.service import reflection_service, health_service
from lib.utils import block_print, wait_for_exit
from delphai_backend_utils import logging
from proto.service_pb2 import _CONSENSUS
import sys, signal, threading
block_print()

app = App(services=[_CONSENSUS, reflection_service, health_service])


@app.method('delphai.consensus.Consensus')
def get_consensus(options, **kwargs):
  return {'company': options['wikipedia']}


if __name__ == "__main__":
  logging.info('starting grpc server...')
  server = Server(app, port='8080')
  server.run(wait=False)
  logging.info('started grpc server')
  wait_for_exit()
