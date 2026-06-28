from pydantic import BaseModel


class SocialMediaResponse(BaseModel):

    linkedin_post: str

    twitter_post: str

    facebook_post: str

    instagram_post: str

    suggested_groups: list[str]

    image_prompt: str

    class Config:
        from_attributes = True