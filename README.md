---
toc: false
fontsize: 36
linkcolor: blue
---

# Deploy a Machine-Learning Model

_Per l'italiano [vedi sotto](#deployare-un-modello-di-machine-learning)_

This challenge takes a solved problem -- training and serving a machine learning model -- and ports it into the domain of operations: MLOps.
A successful candidate will demonstrate ability to take artifacts (ML application and model) and render them operable.

## Objectives

We define a single primary objective which determines a PASS/FAIL, and several secondary objectives which qualify the result.

**Primary Objective**: Serve model predictions from a trained model for future behavior via a REST interface.

**Secondary Objectives**:

1. Train a model with training data and relevant machine learning model.
1. Package the model into a relevant format.
1. Construct an API which serves predictions using FastAPI on a `/predict` endpoint.
1. Package model and application serving the API into appropriate containers
1. Create an artifact for deployment into a Kubernetes cluster (Helm Chart)
1. Implement telmetry for the model performance and expose at least 1 metric on the `/health` endpoint
1. Write at least 1 functional test for the model to verify that the primary objective has been achieved, and one stress test to demonstrate performance under load

## Requirements

A repository has been created for you in GitHub and you have been invited to join it as contributor.
By accepting the invitation to the repository, you will have access to the repository which we will use to evaluate your challenge.
We expect the challenge to be completed within 10 business days unless otherwise specified; an extension can be requested under certain circumstances (see [Communicating with Kiratech](#communicating-with-kiratech) below)

The following requirements apply to the evaluation:

1. Only the contents of the repository will be used for evaluation.
1. You must use the classification method provided in the sample
1. The model must be trained on the training dataset
1. The model must be exposed by FastAPI
1. Changes to the code and model must be tested (see [Continuous Integration](#continuous-integration) below)
1. The entire solution must be implemented as code. Declarative formats are favoured
1. Supporting the code itself, provide a README and relevant comments in the code.

## Completing the Challenge

### Model training

In the context of our challenge, candidates are required to demonstrate their foundational knowledge of machine learning. We suggest you to train at least 2 models and choose one of them, justifying your approach and your choice of the best model. The solution shouldn’t be very complex.

### Application deployment

In a production environment, the application will eventually be deployed into a cloud-native environment.
This very often a Kubernetes cluster.
[Helm](https://helm.sh) is often used as a package manager for Kubernetes workloads.

You are not required to create a fully-working cluster, but need to have a working knowledge of Kubernetes primitives in order to write the Helm chart mentioned above.

### Approach

We evaluate not only the final result of the challenge, but also your approach.
We suggest that candidates who attempt the challenge make their decisions explicit and verbose.

### Source Control

We will evaluate the entire history of the repository's source, including issues and pull-requests -- we want to see how you work, not just the final product.
If you have adopted a method for versioning, commit messages, pipeline stages, _etc_ then make explicit reference to this in the README.

### Continuous Integration

Implement at least 2 stages of continuous integration, showing how you would protect against deploys of broken or incomplete code.
Produce a series of versioned artifacts which can be considered immutable and production ready.
We suggest using Github Actions and Github packages for this purpose, but alternatives will not be penalised so long as they can be verified and are justified.

## Communicating with Kiratech

Kiratech Engineering Management staff will act as _observers_ of the repository for evaluation purposes.
You may communicate with Kiratech to clarify any technical aspect, via email.
Kiratech will not monitor or respond to issues or pull requests.

# Deployare un modello di machine learning

Questa sfida prende un problema risolto (addestrare e servire un modello di machine learning) e lo porta nel dominio delle operazioni: MLOps.
Un candidato prescelto dimostrerà la capacità di prendere artefatti (applicazione e modello ML) e renderli utilizzabili.

## Obiettivi

Definiamo un unico obiettivo primario che determina un PASS/FAIL, e diversi obiettivi secondari che qualificano il risultato.

**Obiettivo primario**: fornire previsioni del modello da un modello addestrato per il comportamento futuro tramite un'interfaccia REST.

**Obiettivi secondari**:

1. Addestrare un modello con dati di addestramento e modello di machine learning pertinente.
1. Creare un pacchetto del modello in un formato pertinente.
1. Costruisci un'API che fornisca previsioni utilizzando FastAPI su un endpoint `/predict`.
1. Pacchetto modello e applicazione che servono l'API in contenitori appropriati
1. Crea un artefatto per la distribuzione in un cluster Kubernetes (diagramma Helm)
1. Implementare la telemetria per le prestazioni del modello ed esporre almeno 1 parametro sull'endpoint "/health".
1. Scrivere almeno 1 test funzionale per il modello per verificare che l'obiettivo primario sia stato raggiunto e uno stress test per dimostrare le prestazioni sotto carico

## Requisiti

È stato creato questo repository per te in GitHub e sei stato invitato a unirti ad esso come collaboratore.
Accettando l'invito al repository, avrai accesso al repository che utilizzeremo per valutare la tua sfida.
Prevediamo che la sfida venga completata entro 10 giorni lavorativi se non diversamente specificato; una proroga può essere richiesta in determinate circostanze (vedi [Comunicare con Kiratech](#communicating-with-kiratech) di seguito)

Per la valutazione valgono i seguenti requisiti:

1. Solo il contenuto del repository verrà utilizzato per la valutazione.
1. È necessario utilizzare il metodo di classificazione fornito nel campione
1. Il modello deve essere addestrato sul set di dati di addestramento
1. Il modello deve essere esposto da FastAPI
1. Le modifiche al codice e al modello devono essere testate (vedi [Integrazione continua](#integrazione-continua-ci) di seguito)
1. L'intera soluzione deve essere implementata come codice. Sono preferiti i formati dichiarativi
1. Supportando il codice stesso, fornire un README e i commenti pertinenti nel codice.

## Completamento della sfida

### Addestramento del modello

Nel contesto di questa sfida, i candidati devono dimostrare la loro conoscenza di base di machine learning. Ti suggeriamo di addestrare minimo 2 modelli e sceglierne uno tra questi, giustificando il tuo approccio e la tua scelta del modello migliore. La soluzione non necessità di essere complessa.

### Distribuzione dell'applicazione

In un ambiente di produzione, l'applicazione verrà infine distribuita in un ambiente nativo del cloud.
Questo molto spesso è un cluster Kubernetes.
[Helm](https://helm.sh) viene spesso utilizzato come gestore di pacchetti per i carichi di lavoro Kubernetes.

Non è necessario creare un cluster completamente funzionante, ma è necessario avere una conoscenza pratica delle primitive Kubernetes per scrivere il grafico Helm menzionato sopra.

### Approccio

Valutiamo non solo il risultato finale della sfida, ma anche il tuo approccio.
Suggeriamo che i candidati che tentano la sfida rendano le loro decisioni esplicite e dettagliate.

### Controllo della fonte (SCM)

Valuteremo l'intera cronologia del sorgente del repository, inclusi problemi e richieste pull: vogliamo vedere come lavori, non solo il prodotto finale.
Se hai adottato un metodo per il controllo delle versioni, i messaggi di commit, le fasi della pipeline, _etc_, fai esplicito riferimento a questo nel README.

### Integrazione continua (CI)

Implementa almeno 2 fasi di integrazione continua, mostrando come proteggerti dalle distribuzioni di codice non funzionante o incompleto.
Produrre una serie di artefatti con versione che possano essere considerati immutabili e pronti per la produzione.
Suggeriamo di utilizzare Github Actions e pacchetti Github per questo scopo, ma le alternative non saranno penalizzate purché possano essere verificate e siano giustificate.

## Comunicare con Kiratech

Il personale di Kiratech Engineering Management fungerà da _osservatore_ del repository a fini di valutazione.
È possibile comunicare con Kiratech per chiarire qualsiasi aspetto tecnico, via e-mail.
Kiratech non monitorerà né risponderà a issues o PR.
