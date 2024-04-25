import ast
from ast import Import, ImportFrom
from importlib import metadata
from pathlib import Path
from sys import stdlib_module_names


def get_module_dependencies(module_path: Path) -> list[Import | ImportFrom]:
    with module_path.open("r") as buffer:
        content = buffer.read()

    parsed_module = ast.parse(content)
    module_body = parsed_module.body
    imports = list(filter(lambda x: isinstance(x, Import | ImportFrom), module_body))
    return imports


def _split_import_types(
    modules: list[Import | ImportFrom],
) -> tuple[list[Import | None], list[ImportFrom | None]]:
    imports: list[Import | None] = list(
        filter(lambda x: isinstance(x, Import), modules)
    )
    imported_froms: list[ImportFrom | None] = list(
        filter(lambda x: isinstance(x, ImportFrom), modules)
    )
    return imports, imported_froms


def filter_python_builtin_modules(
    modules: list[Import | ImportFrom],
) -> list[Import | ImportFrom | None]:
    imports, imported_froms = _split_import_types(modules)

    clean_imports = list(
        filter(
            lambda x: any(alias in stdlib_module_names for alias in x.names),
            imports,
        )
    )

    clean_imported_froms = list(
        filter(
            lambda x: x.module not in stdlib_module_names,
            imported_froms,
        )
    )
    return clean_imports + clean_imported_froms


def _get_third_party_dependencies() -> list[str]:
    return list(map(lambda x: x.metadata["Name"], metadata.distributions()))


def filter_third_party_dependencies(
    modules: list[Import | ImportFrom],
) -> list[Import | ImportFrom | None]:
    third_party_dependencies = _get_third_party_dependencies()
    imports, imported_froms = _split_import_types(modules)

    clean_imports = list(
        filter(
            lambda x: any(alias in third_party_dependencies for alias in x.names),
            imports,
        )
    )

    clean_imported_froms = list(
        filter(
            lambda x: x.module not in third_party_dependencies,
            imported_froms,
        )
    )
    return clean_imports + clean_imported_froms
