# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class TagUpdateTagsTags(BaseModel):
    """Information about the tag.

    :param slug: The tag's ID within a team or individual (non-team) user scope.
    :type slug: str
    """

    def __init__(self, slug: str):
        """Information about the tag.

        :param slug: The tag's ID within a team or individual (non-team) user scope.
        :type slug: str
        """
        self.slug = self._define_str(
            "slug",
            slug,
            pattern="^[a-z][a-z0-9-]*[a-z0-9]+$",
            min_length=2,
            max_length=64,
        )


@JsonMap({})
class TagUpdateTags(BaseModel):
    """TagUpdateTags

    :param tags: A list of the associated tags as slugs.
    :type tags: List[TagUpdateTagsTags]
    """

    def __init__(self, tags: List[TagUpdateTagsTags]):
        """TagUpdateTags

        :param tags: A list of the associated tags as slugs.
        :type tags: List[TagUpdateTagsTags]
        """
        self.tags = self._define_list(tags, TagUpdateTagsTags)
