# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T09:25:57+00:00

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from . import DefsOkFalse, DefsOkTrue


class StepCompletedGetResponse(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    ok: DefsOkTrue


class StepCompletedGetResponseModel(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    ok: DefsOkFalse


class StepFailedGetResponse(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    ok: DefsOkTrue


class StepFailedGetResponseModel(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    ok: DefsOkFalse


class UpdateStepGetResponse(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    ok: DefsOkTrue


class UpdateStepGetResponseModel(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    ok: DefsOkFalse
