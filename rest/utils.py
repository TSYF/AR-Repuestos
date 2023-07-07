from rest_framework import status
from rest_framework.response import Response


HTTP_RESPONSE_MAP = {
    200: {
        "status": "OK",
        "OK": True,
        "enum": status.HTTP_200_OK
    },
    201: {
        "status": "CREATED",
        "OK": True,
        "enum": status.HTTP_201_CREATED
    },
    202: {
        "status": "ACCEPTED",
        "OK": True,
        "enum": status.HTTP_202_ACCEPTED
    },
    203: {
        "status": "NON_AUTHORITATIVE_INFORMATION",
        "OK": True,
        "enum": status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
    },
    204: {
        "status": "NO_CONTENT",
        "OK": True,
        "enum": status.HTTP_204_NO_CONTENT
    },
    205: {
        "status": "RESET_CONTENT",
        "OK": True,
        "enum": status.HTTP_205_RESET_CONTENT
    },
    206: {
        "status": "PARTIAL_CONTENT",
        "OK": True,
        "enum": status.HTTP_206_PARTIAL_CONTENT
    },
    207: {
        "status": "MULTI_STATUS",
        "OK": True,
        "enum": status.HTTP_207_MULTI_STATUS
    },
    208: {
        "status": "ALREADY_REPORTED",
        "OK": True,
        "enum": status.HTTP_208_ALREADY_REPORTED
    },
    226: {
        "status": "IM_USED",
        "OK": True,
        "enum": status.HTTP_226_IM_USED
    },
    400: {
        "status": "BAD_REQUEST",
        "OK": False,
        "enum": status.HTTP_400_BAD_REQUEST
    },
    401: {
        "status": "UNAUTHORIZED",
        "OK": False,
        "enum": status.HTTP_401_UNAUTHORIZED
    },
    402: {
        "status": "PAYMENT_REQUIRED",
        "OK": False,
        "enum": status.HTTP_402_PAYMENT_REQUIRED
    },
    403: {
        "status": "FORBIDDEN",
        "OK": False,
        "enum": status.HTTP_403_FORBIDDEN
    },
    404: {
        "status": "NOT_FOUND",
        "OK": False,
        "enum": status.HTTP_404_NOT_FOUND
    },
    405: {
        "status": "METHOD_NOT_ALLOWED",
        "OK": False,
        "enum": status.HTTP_405_METHOD_NOT_ALLOWED
    },
    406: {
        "status": "NOT_ACCEPTABLE",
        "OK": False,
        "enum": status.HTTP_406_NOT_ACCEPTABLE
    },
    407: {
        "status": "PROXY_AUTHENTICATION_REQUIRED",
        "OK": False,
        "enum": status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED
    },
    408: {
        "status": "REQUEST_TIMEOUT",
        "OK": False,
        "enum": status.HTTP_408_REQUEST_TIMEOUT
    },
    409: {
        "status": "CONFLICT",
        "OK": False,
        "enum": status.HTTP_409_CONFLICT
    },
    410: {
        "status": "GONE",
        "OK": False,
        "enum": status.HTTP_410_GONE
    },
    411: {
        "status": "LENGTH_REQUIRED",
        "OK": False,
        "enum": status.HTTP_411_LENGTH_REQUIRED
    },
    412: {
        "status": "PRECONDITION_FAILED",
        "OK": False,
        "enum": status.HTTP_412_PRECONDITION_FAILED
    },
    413: {
        "status": "REQUEST_ENTITY_TOO_LARGE",
        "OK": False,
        "enum": status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
    },
    414: {
        "status": "REQUEST_URI_TOO_LONG",
        "OK": False,
        "enum": status.HTTP_414_REQUEST_URI_TOO_LONG
    },
    415: {
        "status": "UNSUPPORTED_MEDIA_TYPE",
        "OK": False,
        "enum": status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    },
    416: {
        "status": "REQUESTED_RANGE_NOT_SATISFIABLE",
        "OK": False,
        "enum": status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
    },
    417: {
        "status": "EXPECTATION_FAILED",
        "OK": False,
        "enum": status.HTTP_417_EXPECTATION_FAILED
    },
    418: {
        "status": "I_AM_A_TEAPOT",
        "OK": False,
        "enum": status.HTTP_418_IM_A_TEAPOT
    },
    422: {
        "status": "UNPROCESSABLE_ENTITY",
        "OK": False,
        "enum": status.HTTP_422_UNPROCESSABLE_ENTITY
    },
    423: {
        "status": "LOCKED",
        "OK": False,
        "enum": status.HTTP_423_LOCKED
    },
    424: {
        "status": "FAILED_DEPENDENCY",
        "OK": False,
        "enum": status.HTTP_424_FAILED_DEPENDENCY
    },
    426: {
        "status": "UPGRADE_REQUIRED",
        "OK": False,
        "enum": status.HTTP_426_UPGRADE_REQUIRED
    },
    428: {
        "status": "PRECONDITION_REQUIRED",
        "OK": False,
        "enum": status.HTTP_428_PRECONDITION_REQUIRED
    },
    429: {
        "status": "TOO_MANY_REQUESTS",
        "OK": False,
        "enum": status.HTTP_429_TOO_MANY_REQUESTS
    },
    431: {
        "status": "REQUEST_HEADER_FIELDS_TOO_LARGE",
        "OK": False,
        "enum": status.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
    },
    451: {
        "status": "UNAVAILABLE_FOR_LEGAL_REASONS",
        "OK": False,
        "enum": status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
    },
    500: {
        "status": "INTERNAL_SERVER_ERROR",
        "OK": False,
        "enum": status.HTTP_500_INTERNAL_SERVER_ERROR
    },
    501: {
        "status": "NOT_IMPLEMENTED",
        "OK": False,
        "enum": status.HTTP_501_NOT_IMPLEMENTED
    },
    502: {
        "status": "BAD_GATEWAY",
        "OK": False,
        "enum": status.HTTP_502_BAD_GATEWAY
    },
    503: {
        "status": "SERVICE_UNAVAILABLE",
        "OK": False,
        "enum": status.HTTP_503_SERVICE_UNAVAILABLE
    },
    504: {
        "status": "GATEWAY_TIMEOUT",
        "OK": False,
        "enum": status.HTTP_504_GATEWAY_TIMEOUT
    },
    505: {
        "status": "HTTP_VERSION_NOT_SUPPORTED",
        "OK": False,
        "enum": status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED
    },
    506: {
        "status": "VARIANT_ALSO_NEGOTIATES",
        "OK": False,
        "enum": status.HTTP_506_VARIANT_ALSO_NEGOTIATES
    },
    507: {
        "status": "INSUFFICIENT_STORAGE",
        "OK": False,
        "enum": status.HTTP_507_INSUFFICIENT_STORAGE
    },
    508: {
        "status": "LOOP_DETECTED",
        "OK": False,
        "enum": status.HTTP_508_LOOP_DETECTED
    },
    510: {
        "status": "NOT_EXTENDED",
        "OK": False,
        "enum": status.HTTP_510_NOT_EXTENDED
    },
    511: {
        "status": "NETWORK_AUTHENTICATION_REQUIRED",
        "OK": False,
        "enum": status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED
    }
}

HTTP_200S = (200, 201, 202, 203, 204, 205, 206, 207, 208, 226)
HTTP_400S = (400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 422, 423, 424, 426, 428, 429, 431, 451)
HTTP_500S = (500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511)

def construct_drf_response(payload, code = 200):
    response = {}
    
    if code in HTTP_200S:
        response = {
            "status": HTTP_RESPONSE_MAP[code]["status"],
            "data": payload,
            "code": code,
            "OK": HTTP_RESPONSE_MAP[code]["OK"]
        }
    
    if code in (*HTTP_400S, *HTTP_500S):
        response = {
            "status": HTTP_RESPONSE_MAP[code]["status"],
            "error": payload,
            "code": code,
            "OK": HTTP_RESPONSE_MAP[code]["OK"]
        }

    return Response( response, HTTP_RESPONSE_MAP[code]["enum"] )