from pydantic import BaseModel

class ExampleText(BaseModel):
    text: str = """
As the sun goes down, a kinda sad feeling fills the air, like a quiet song playing in the background. 
The sky turns all orange and paints a picture that's both a little happy and a little sad. 
A gentle breeze comes by, bringing back memories that make your heart feel a mix of things—like 
remembering something sweet but also a bit sad. Right now, everything feels important, like a big 
mashup of love and missing something. It's like a beautiful moment that's here and then gone, 
leaving you with feelings that are hard to put into words. And as the stars start 
to show up in the dark sky, it's like your feelings are opening up, just like flowers in a garden.
"""

    