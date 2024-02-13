import 'dart:async';
import 'dart:convert';
import 'package:django_backend_api/django_backend_api.dart';
import 'package:authentication_api/authentication_api.dart';

enum AuthenticationStatus { unknown, authenticated, unauthenticated }

class AuthenticationRepository {
  final _controller = StreamController<AuthenticationStatus>();

  Stream<AuthenticationStatus> get status async* {
    await Future<void>.delayed(const Duration(seconds: 1));
    yield AuthenticationStatus.unauthenticated;
    yield* _controller.stream;
  }

  // Future<void> logIn({
  //   required String username,
  //   required String password,
  // }) async {
  //   await Future.delayed(
  //     const Duration(milliseconds: 300),
  //     () => _controller.add(AuthenticationStatus.authenticated),
  //   );
  // }

  void logOut() async {
    _controller.add(AuthenticationStatus.unauthenticated);
  }

  Future<String> logIn(
      AuthenticationApi auth, String username, String password) async {
    try {
      final String apiKey =
          await auth.logIn(username: username, password: password);
      _controller.add(AuthenticationStatus.authenticated);

      return apiKey;
    } catch (e) {
      _controller.add(AuthenticationStatus.unauthenticated);
      return '';
    }
  }

  void dispose() => _controller.close();
}
