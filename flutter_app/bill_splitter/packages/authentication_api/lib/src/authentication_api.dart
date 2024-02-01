/// {@template authentication_api}
/// Abstraction for authentication API
/// {@endtemplate}
abstract class AuthenticationApi<T> {
  /// {@macro authentication_api}
  const AuthenticationApi();

  T logIn({required String username, required String password});

  void logOut();
}
