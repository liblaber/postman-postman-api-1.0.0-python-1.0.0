from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class UpdateApiTagsRequestTags(BaseModel):
    """Information about the tag.

    :param slug: The tag's ID within a team or individual (non-team) user scope.
    :type slug: str
    """

    def __init__(self, slug: str):
        self.slug = self._pattern_matching(slug, "^[a-z][a-z0-9-]*[a-z0-9]+$", "slug")


@JsonMap({})
class UpdateApiTagsRequest(BaseModel):
    """UpdateApiTagsRequest

    :param tags: A list of the associated tags as slugs.
    :type tags: List[UpdateApiTagsRequestTags]
    """

    def __init__(self, tags: List[UpdateApiTagsRequestTags]):
        self.tags = self._define_list(tags, UpdateApiTagsRequestTags)
