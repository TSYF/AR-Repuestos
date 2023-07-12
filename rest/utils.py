from rest_framework import status
from rest_framework.response import Response


HTTP_RESPONSE_MAP = {
    200: {
        "status": "OK",
        "enum": status.HTTP_200_OK
    },
    201: {
        "status": "CREATED",
        "enum": status.HTTP_201_CREATED
    },
    202: {
        "status": "ACCEPTED",
        "enum": status.HTTP_202_ACCEPTED
    },
    203: {
        "status": "NON_AUTHORITATIVE_INFORMATION",
        "enum": status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
    },
    204: {
        "status": "NO_CONTENT",
        "enum": status.HTTP_204_NO_CONTENT
    },
    205: {
        "status": "RESET_CONTENT",
        "enum": status.HTTP_205_RESET_CONTENT
    },
    206: {
        "status": "PARTIAL_CONTENT",
        "enum": status.HTTP_206_PARTIAL_CONTENT
    },
    207: {
        "status": "MULTI_STATUS",
        "enum": status.HTTP_207_MULTI_STATUS
    },
    208: {
        "status": "ALREADY_REPORTED",
        "enum": status.HTTP_208_ALREADY_REPORTED
    },
    226: {
        "status": "IM_USED",
        "enum": status.HTTP_226_IM_USED
    },
    400: {
        "status": "BAD_REQUEST",
        "enum": status.HTTP_400_BAD_REQUEST
    },
    401: {
        "status": "UNAUTHORIZED",
        "enum": status.HTTP_401_UNAUTHORIZED
    },
    402: {
        "status": "PAYMENT_REQUIRED",
        "enum": status.HTTP_402_PAYMENT_REQUIRED
    },
    403: {
        "status": "FORBIDDEN",
        "enum": status.HTTP_403_FORBIDDEN
    },
    404: {
        "status": "NOT_FOUND",
        "enum": status.HTTP_404_NOT_FOUND
    },
    405: {
        "status": "METHOD_NOT_ALLOWED",
        "enum": status.HTTP_405_METHOD_NOT_ALLOWED
    },
    406: {
        "status": "NOT_ACCEPTABLE",
        "enum": status.HTTP_406_NOT_ACCEPTABLE
    },
    407: {
        "status": "PROXY_AUTHENTICATION_REQUIRED",
        "enum": status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED
    },
    408: {
        "status": "REQUEST_TIMEOUT",
        "enum": status.HTTP_408_REQUEST_TIMEOUT
    },
    409: {
        "status": "CONFLICT",
        "enum": status.HTTP_409_CONFLICT
    },
    410: {
        "status": "GONE",
        "enum": status.HTTP_410_GONE
    },
    411: {
        "status": "LENGTH_REQUIRED",
        "enum": status.HTTP_411_LENGTH_REQUIRED
    },
    412: {
        "status": "PRECONDITION_FAILED",
        "enum": status.HTTP_412_PRECONDITION_FAILED
    },
    413: {
        "status": "REQUEST_ENTITY_TOO_LARGE",
        "enum": status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
    },
    414: {
        "status": "REQUEST_URI_TOO_LONG",
        "enum": status.HTTP_414_REQUEST_URI_TOO_LONG
    },
    415: {
        "status": "UNSUPPORTED_MEDIA_TYPE",
        "enum": status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    },
    416: {
        "status": "REQUESTED_RANGE_NOT_SATISFIABLE",
        "enum": status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
    },
    417: {
        "status": "EXPECTATION_FAILED",
        "enum": status.HTTP_417_EXPECTATION_FAILED
    },
    418: {
        "status": "I_AM_A_TEAPOT",
        "enum": status.HTTP_418_IM_A_TEAPOT
    },
    422: {
        "status": "UNPROCESSABLE_ENTITY",
        "enum": status.HTTP_422_UNPROCESSABLE_ENTITY
    },
    423: {
        "status": "LOCKED",
        "enum": status.HTTP_423_LOCKED
    },
    424: {
        "status": "FAILED_DEPENDENCY",
        "enum": status.HTTP_424_FAILED_DEPENDENCY
    },
    426: {
        "status": "UPGRADE_REQUIRED",
        "enum": status.HTTP_426_UPGRADE_REQUIRED
    },
    428: {
        "status": "PRECONDITION_REQUIRED",
        "enum": status.HTTP_428_PRECONDITION_REQUIRED
    },
    429: {
        "status": "TOO_MANY_REQUESTS",
        "enum": status.HTTP_429_TOO_MANY_REQUESTS
    },
    431: {
        "status": "REQUEST_HEADER_FIELDS_TOO_LARGE",
        "enum": status.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
    },
    451: {
        "status": "UNAVAILABLE_FOR_LEGAL_REASONS",
        "enum": status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
    },
    500: {
        "status": "INTERNAL_SERVER_ERROR",
        "enum": status.HTTP_500_INTERNAL_SERVER_ERROR
    },
    501: {
        "status": "NOT_IMPLEMENTED",
        "enum": status.HTTP_501_NOT_IMPLEMENTED
    },
    502: {
        "status": "BAD_GATEWAY",
        "enum": status.HTTP_502_BAD_GATEWAY
    },
    503: {
        "status": "SERVICE_UNAVAILABLE",
        "enum": status.HTTP_503_SERVICE_UNAVAILABLE
    },
    504: {
        "status": "GATEWAY_TIMEOUT",
        "enum": status.HTTP_504_GATEWAY_TIMEOUT
    },
    505: {
        "status": "HTTP_VERSION_NOT_SUPPORTED",
        "enum": status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED
    },
    506: {
        "status": "VARIANT_ALSO_NEGOTIATES",
        "enum": status.HTTP_506_VARIANT_ALSO_NEGOTIATES
    },
    507: {
        "status": "INSUFFICIENT_STORAGE",
        "enum": status.HTTP_507_INSUFFICIENT_STORAGE
    },
    508: {
        "status": "LOOP_DETECTED",
        "enum": status.HTTP_508_LOOP_DETECTED
    },
    510: {
        "status": "NOT_EXTENDED",
        "enum": status.HTTP_510_NOT_EXTENDED
    },
    511: {
        "status": "NETWORK_AUTHENTICATION_REQUIRED",
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
            "OK": True
        }
    
    if code in (*HTTP_400S, *HTTP_500S):
        response = {
            "status": HTTP_RESPONSE_MAP[code]["status"],
            "error": payload,
            "code": code,
            "OK": False
        }

    return Response( response, HTTP_RESPONSE_MAP[code]["enum"] )