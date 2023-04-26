import typing

from pydantic import Field, BaseModel
from autotest.schemas.base import BaseSchema


class ProjectIn(BaseModel):
    id: int = Field(None, description="id")
    name: str = Field(..., description="项目名称")
    test_user: str = Field(None, description="测试人员")
    responsible_name: str = Field(None, description="负责人")
    dev_user: str = Field(None, description="开发人员")
    publish_app: str = Field(None, description="发布应用")
    simple_desc: str = Field(None, description="简要描述")
    remarks: str = Field(None, description="其他信息'")
    config_id: int = Field(None, description="关联配置id'")


class ProjectQuery(BaseSchema):
    """查询参数序列化"""

    id: int = Field(None, description="id")
    ids: typing.List = Field(None, description="id 列表")
    name: str = Field(None, description="项目名称")
    order_field: str = Field(None, description="排序字段")
    sort_type: str = Field(None, description="排序类型")
    created_by_name: str = Field(None, description="创建人名称")


class ProjectId(BaseSchema):
    """删除"""

    id: int = Field(..., description="id")
