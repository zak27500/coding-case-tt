from enum import StrEnum

from pydantic import BaseModel, Field


class Message(BaseModel):
    id: str
    debut_secondes: int
    locuteur: str
    texte: str


class Entretien(BaseModel):
    id: str
    clien_id: str
    titre: str
    langue: str
    source: str
    messages: list[Message]


class StatutExecution(StrEnum):
    OK = "ok"
    DEGRADE = "degrade"
    ERREUR = "erreur"


class Regle(BaseModel):
    id: str
    titre: str
    question: str


class Controle(BaseModel):
    version: str
    regles: list[Regle]


class Produit(BaseModel):
    id: str
    nom: str
    famille: str
    type: str
    prix_mensuel_eur: int
    besoins_couverts: list[str]
    conditions: list[str]
    exclusions: list[str]
    limites: list[str]
    prerequis_produit_ids: list[str] = Field(default_factory=list)
    documents_id: list[str]


class Diagnostic(BaseModel):
    mode: str
    modele: str
    appel_modele_effectue: bool
    duree_ms: int
    avertsissements: list[str]


class Reference(BaseModel):
    doc_id: str
    section_id: str


class Rapport(BaseModel):
    entretien_id: str
    statut_execution: StatutExecution
    synthese: str
    besoins: list[str] = Field(default_factory=list)
    controles: list[Controle]
    recommendations: list[Produit] = Field(default_factory=list)
    sources_documentaires: list[Reference]
    quetsions_a_poser: list[str] = Field(default_factory=list)
    diagnostic: Diagnostic
