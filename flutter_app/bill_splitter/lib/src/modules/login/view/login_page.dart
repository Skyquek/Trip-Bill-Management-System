import 'package:authentication_repository/authentication_repository.dart';
import 'package:bill_splitter/src/modules/login/bloc/login_bloc.dart';
import 'package:bill_splitter/src/modules/login/view/login_form.dart';
import 'package:django_backend_api/django_backend_api.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class LoginPage extends StatelessWidget {
  const LoginPage({super.key});

  static Route<void> route() {
    return MaterialPageRoute<void>(builder: (_) => const LoginPage());
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(12),
        child: BlocProvider(
          create: (context) {
            return LoginBloc(
              authMechanism: DjangoUserAuthApi(),
              authenticationRepository:
                  RepositoryProvider.of<AuthenticationRepository>(context),
            );
          },
          child: const LoginForm(),
        ),
      ),
    );
  }
}
