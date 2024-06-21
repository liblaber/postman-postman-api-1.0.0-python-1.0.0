from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class GetApiTagsOkResponseTags(BaseModel):
    """Information about the tag.

    :param slug: The tag's ID within a team or individual (non-team) user scope., defaults to None
    :type slug: str, optional
    """

    def __init__(self, slug: str = None):
        if slug is not None:
            self.slug = self._pattern_matching(
                slug, "^[a-z][a-z0-9-]*[a-z0-9]+$", "slug"
            )


@JsonMap({})
class GetApiTagsOkResponse(BaseModel):
    """GetApiTagsOkResponse

    :param tags: A list of associated tags., defaults to None
    :type tags: List[GetApiTagsOkResponseTags], optional
    """

    def __init__(self, tags: List[GetApiTagsOkResponseTags] = None):
        if tags is not None:
            self.tags = self._define_list(tags, GetApiTagsOkResponseTags)
