package console.utils;

import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.stream.Collectors;

public class ValidCommands {
  // --- Command definitions ---
  private static final Set<String> menuCommands = Set.of(
          "help", "start", "delete", "games", "exit", "quit"
  );


  // --- Wrappers ---
  public static final Set<String> MENU_COMMANDS =
          toUnmodifiableLowercaseSet(menuCommands);

  // --- Global collector ---
  public static final Set<String> ALL_COMMANDS = collectAllCommandSets();


  // --- Helpers ---
  private static Set<String> toUnmodifiableLowercaseSet(Set<String> input) {
    return Collections.unmodifiableSet(
            (Set<? extends String>) input.stream()
                    .map(String::toLowerCase)
                    .collect(Collectors.toCollection(LinkedHashSet::new))
    );
  }


  private static Set<String> collectAllCommandSets() {
    Set<String> all = new HashSet<>();
    try {
      for (Field field : ValidCommands.class.getDeclaredFields()) {
        // Collect only uppercase public sets
        if (Modifier.isStatic(field.getModifiers())
                && Modifier.isFinal(field.getModifiers())
                && Set.class.isAssignableFrom(field.getType())
                && field.getName().equals(field.getName().toUpperCase()) // only uppercase
                && !field.getName().equals("ALL_COMMANDS")) { // skip self
          @SuppressWarnings("unchecked")
          Set<String> subset = (Set<String>) field.get(null);
          all.addAll(subset);
        }
      }
    } catch (IllegalAccessException e) {
      throw new RuntimeException("Reflection failed while collecting commands", e);
    }
    return Collections.unmodifiableSet(all);
  }
}
