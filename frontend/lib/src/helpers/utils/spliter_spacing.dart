import 'package:flutter/material.dart';

// TODO(Quek): create more of my custom spacing
class SplitterSpacing {
  static double safeAreaTop(BuildContext context) {
    return MediaQuery.of(context).padding.top;
  }
}
