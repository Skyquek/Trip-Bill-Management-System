import 'dart:async';

import 'package:user_repository/user_repository.dart';

class UserRepository {
  User? _user;

  Future<User?> getUser() async {
    if (_user != null) return _user;

    return Future.delayed(
      const Duration(milliseconds: 300),
      () {
        // TODO(Quek): this part need to change to django_backend data provider.
        return _user = User('001', 'yj', 'yao jing', 'quek');
      },
    );
  }
}
