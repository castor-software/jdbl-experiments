import os
import subprocess

from core.PomExtractor import PomExtractor
from core.Project import Project


class Debloat:
    def __init__(self, project:Project):
        self.project = project

    def inject_library(self):
        (includes, excludes) = self.project.pom.get_included_excluded_tests()
        exclude_config = []
        for exclude in excludes:
            exclude_config.append({
                "name": "exclude",
                "text": exclude
            })
        include_config = []
        for include in includes:
            include_config.append({
                "name": "include",
                "text": include
            })
        self.project.pom.add_plugin("org.apache.maven.plugins", "maven-surefire-plugin", "2.19.1", [{
            "name": "configuration",
            "children": [
                {
                    "name": "excludes",
                    "children": exclude_config
                },
                {
                    "name": "includes",
                    "children": include_config
                }
            ]
        }])
        self.project.pom.add_plugin("se.kth.castor", "jdbl-maven-plugin", "1.0.0", [{
            "name": "executions",
            "children": [
                {
                    "name": "execution",
                    "children": [
                        {
                            "name": "goals",
                            "children": [
                                {
                                    "name": "goal",
                                    "text": "test-based-debloat"
                                }
                            ]
                        }
                    ]
                }
            ]
        }])
        

        self.project.pom.write_pom()
        pass

    def run(self, stdout:str=None):
        self.inject_library()
        return self.project.package(stdout=stdout)
