"""Methods for the interest group cross-origin permissions endpoint."""
import json

from fledge.tentative.resources import fledge_http_server_util

def get_permissions(request, response):
  """Returns JSON object containing interest group cross-origin permissions.

  The structure returned is described in more detail at
  https://github.com/WICG/turtledove/blob/main/FLEDGE.md#13-permission-delegation.
  This correctly handles requests issued in CORS mode.

  This currently always returns True for both join and leave.
  """
  if fledge_http_server_util.handle_cors_headers_and_preflight(request, response):
    return

  response.status = (200, b"OK")
  response.headers.set(b"Content-Type", b"application/json")
  response.content = json.dumps({
    "joinAdInterestGroup": True,
    "leaveAdInterestGroup": True
  })

