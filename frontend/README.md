# bill_splitter

A new Flutter project.

## Flutter Bloc

- Presentation: The presentation layer's responsibility is to figure out how to render itself based on one or more bloc states. In addition, it should handle user input and application lifecycle events.
- Business Logic: BLOC, State, and Events
- Data
  - Repository: The repository layer is a wrapper around one or more data providers with which the Bloc Layer communicates.
  - Data Provider: The data provider's responsibility is to provide raw data. The data provider should be generic and versatile. Data Provider/Service/API Client: This component is responsible for making requests to external data sources. It may involve network requests, database queries, or any other method of fetching or storing data.

## Note

- A bloc should only receive information through events and from injected repositories (i.e., repositories given to the bloc in its constructor)
- A bloc shouldn't call other bloc
