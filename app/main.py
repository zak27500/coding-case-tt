from domain import Detention, Message, ProfilClient, Rapport
from llm.qwen import QWENClient
from prompt import format_prompt

if __name__ == "__main__":
    messages = [
        {
            "id": "E01-S01",
            "debut_secondes": 0,
            "locuteur": "agent",
            "texte": "Bonjour, pour quel usage souhaitez-vous assurer votre voiture ?",
        },
        {
            "id": "E01-S02",
            "debut_secondes": 15,
            "locuteur": "client",
            "texte": "Je suis infirmière libérale. Je fais mes tournées avec ma voiture, environ 18 000 kilomètres par an.",
        },
    ]

    profils = [
        {
            "id": "C01",
            "situation_professionnelle": "infirmière libérale",
            "composition_foyer": "1 adulte",
            "budget_mensuel_eur": 65,
            "projets": ["maintenir la mobilité professionnelle"],
            "date_mise_a_jour": "2026-09-01",
        },
        {
            "id": "C02",
            "situation_professionnelle": "salarié",
            "composition_foyer": "2 adultes, 1 enfant",
            "budget_mensuel_eur": 5,
            "projets": ["déménagement en maison comme propriétaire"],
            "date_mise_a_jour": "2026-09-01",
        },
    ]

    detentions = [
        {
            "id": "D01",
            "client_id": "C01",
            "produit_id": "P01",
            "statut": "actif",
            "garanties": ["responsabilite_civile_auto", "assistance_50km"],
            "usage_declare": "privé",
            "prime_mensuelle_eur": 42,
        }
    ]
    messages_model = [Message(**message) for message in messages]
    profiles_clients = [ProfilClient(**profil) for profil in profils]

    detentions_model = [Detention(**detention) for detention in detentions]
    prompt = format_prompt(
        transcription=messages_model,
        profil=profiles_clients[0],
        detentions=detentions_model,
    )
    client = QWENClient()
    reponse = client.complete(prompt)
    response_model = Rapport.model_validate(reponse)
    assert isinstance(response_model, Rapport)
    print(reponse)
    # llm = Llama(
    #     model_path="models/qwen2.5-1.5b-instruct-q4_k_m.gguf",
    #     n_ctx=12000,
    #     n_threads=6,
    #     verbose=False,
    # )
    # out = llm.create_chat_completion(
    #     messages=[{"role": "user", "content": "Dis bonjour en une phrase."}],
    #     temperature=0,
    # )
    # assert isinstance(out, dict)
    # print(out["choices"][0]["message"]["content"])
