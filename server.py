import torch
from pydantic import BaseModel, Field
from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

model_path = './KoGPT2'
tokenizer = PreTrainedTokenizerFast.from_pretrained(model_path, 
                                                    bos_token='</s>', 
                                                    eos_token='</s>', 
                                                    unk_token='<unk>',
                                                    pad_token='<pad>', 
                                                    mask_token='<mask>', 
                                                    from_tf=True,
                                                    local_files_only=True)
model = GPT2LMHeadModel.from_pretrained(model_path, local_files_only=True)
model = model.to(device)


class TextGenerationInput(BaseModel):
    base_text: str = Field(
        ...,
        title="Input Text",
        description="Base text to generate Contents.",
        max_length=100,
    )


class TextGenerationOutput(BaseModel):
    output: str


def generate_korean_contents(input: TextGenerationInput) -> TextGenerationOutput:
    """Generate Korean contents using KoGPT2"""
    query = input.base_text  # base_text
    input_ids = tokenizer.encode(query, return_tensors='pt')
    input_ids = input_ids.to(device)

    # model generating
    sample_outputs = model.generate(input_ids,
                                    do_sample=True,
                                    max_length=128,
                                    no_repeat_ngram_size=2,
                                    top_k=50,
                                    top_p=0.95)


    contents = tokenizer.decode(sample_outputs[0])

    return TextGenerationOutput(output=contents)
