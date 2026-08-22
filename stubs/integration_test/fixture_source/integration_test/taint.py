# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from typing import Any

from django.http import HttpRequest


def source() -> Any:
    request = HttpRequest()
    return request.GET["bad"]


def sink(argument: Any) -> None:
    eval(argument)  # noqa
