# clean-architecture-aws-lambda

## Concepts from clean arch
Layred arechitecture apporach focusing in onion/concentric circle model, putting less stables layers at the borders and more stable layers (domain layer), at the center.

- use cases layer defines the operations the application can handle
- entrypoints points to the use cases
- repositories, external_apis and any other layer in which the domain layer needs to call has its interfaces within the domain layer ( the domain layer points mentions its own structre). Those layers implements the interfaces, pointing to the domain layer.

## concept and patterns from DDD
Aggregates, entities, value objects, policies, services and factories