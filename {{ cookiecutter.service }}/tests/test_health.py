import pytest

from {{ cookiecutter.service }} import methods
import tests


@pytest.mark.asyncio
async def test_create_answer():
    method = methods.Health()
    client = tests.client()
    resp, status = await client.request(method)
    assert status == 204
