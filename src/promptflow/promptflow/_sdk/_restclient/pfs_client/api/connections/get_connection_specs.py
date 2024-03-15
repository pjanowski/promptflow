from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ....utils import _request_wrapper
from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connection_spec import ConnectionSpec
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Connections/specs",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ConnectionSpec]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ConnectionSpec.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ConnectionSpec]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@_request_wrapper()
def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    stream: bool = False,
) -> Response[ConnectionSpec]:
    """List connection spec

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionSpec]
    """

    kwargs = _get_kwargs()

    if stream:
        return client.get_httpx_client().stream(**kwargs)
    else:
        response = client.get_httpx_client().request(
            **kwargs,
        )
        return _build_response(client=client, response=response)


@_request_wrapper()
def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ConnectionSpec]:
    """List connection spec

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionSpec
    """

    return sync_detailed(
        client=client,
    ).parsed


@_request_wrapper()
async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    stream: bool = False,
) -> Response[ConnectionSpec]:
    """List connection spec

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionSpec]
    """

    kwargs = _get_kwargs()
    if stream:
        with await client.get_httpx_client().stream(**kwargs) as response:
            return _build_response(client=client, response=response)
    else:
        response = await client.get_async_httpx_client().request(**kwargs)

        return _build_response(client=client, response=response)


@_request_wrapper()
async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ConnectionSpec]:
    """List connection spec

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionSpec
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed