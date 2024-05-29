from pydantic import BaseModel, Field, ConfigDict
from enum import Enum
from typing import List
from typing import Optional

class LLMModelType(str, Enum):
    """
    OpenAI model type
    """
    gpt_3_5_turbo = "gpt-3.5-turbo-1106"
    gpt_4 = "gpt-4"

class InputItemType(str, Enum):
    """
    OutputArgsType Enum
    """
    string = 'string'
    integer = 'integer'
    float = 'float'
    boolean = 'boolean'
    array = 'array'
class InputItem(BaseModel):
    name: str = Field(
        description='Name of the output argument.',
        json_schema_extra={
            "from_upstream": "never"
        }
    )
    type: InputItemType = Field(
        default=InputItemType.string,
        description='Type of the output argument.',
        json_schema_extra={
            "from_upstream": "never"
        },
    )
    description: str = Field(
        default="",
        description='Description of the output argument.',
        json_schema_extra={
            "from_upstream": "never"
        }
    )

    name: str = Field()
    type: str = Field()
    description: str = Field()

class InputModel(BaseModel):
    """
    InformationExtractionPiece Input model
    """
    input_file_path: str = Field(
        description='Source text from where information should be extracted.',
        json_schema_extra={"from_upstream": "always"}
    )
    additional_information: Optional[str] = Field(
        default=None,
        description='Additional useful information to help with the extraction.',
    )
    openai_model: LLMModelType = Field(
        default=LLMModelType.gpt_3_5_turbo,
        description="OpenAI model name to use for information extraction.",
    )
    extract_items: List[InputItem] = Field(
        default=[
            InputItem(name="name", type=InputItemType.string, description="Name of the person."),
            InputItem(name="age", type=InputItemType.integer, description="Age of the person."),
        ],
        description='Information items to be extracted from source text.',
        json_schema_extra={"from_upstream": "never"}
    )


class OutputModel(BaseModel):
    """
    InformationExtractionPiece Output Model
    """
    output_data: List[dict] = Field(description="Extracted information as JSON.")
    # output_file_path: str = Field(description="Extracted information as json file.")

class SecretsModel(BaseModel):
    """
    InformationExtractionPiece Secrets model
    """
    OPENAI_API_KEY: str = Field(description="Your OpenAI API key.")
