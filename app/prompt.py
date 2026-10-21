import json

from domain import Detention, Message, ProfilClient, Rapport

PROMPT = """

voici le contexte ...
voici la transcription : {messages}
voci le profil client: {profil}
voici les detentions: {detentions}
vocii les regles
voici le format de reponse requis du rapport: {schema}
"""


def format_prompt(
    transcription: list[Message], profil: ProfilClient, detentions: list[Detention]
) -> str:
    messages_str = "\n".join(message.model_dump_json() for message in transcription)
    profil_client_str = profil.model_dump_json()
    detentions_str = "\n".join(detention.model_dump_json() for detention in detentions)
    rapport_schema = json.dumps(Rapport.model_json_schema())
    return PROMPT.format(
        messages=messages_str,
        profil=profil_client_str,
        detentions=detentions_str,
        schema=rapport_schema,
    )
