"""
Author: Lawrence Du
E-mail: larrydu88@gmail.com
"""

from toolchain import CythonRecipe,shprint
import os
from os.path import join
import sh


class CymunkRecipe(CythonRecipe):
    version = 'master'
    url = 'https://github.com/kivy/cymunk/archive/{version}.zip'
    name = 'cymunk'
    pre_build_ext = True
    library = 'libcymunk.a'

    depends = ['python3', 'hostpython']

    def get_recipe_env(self, arch):
        ret = super(CymunkRecipe, self).get_recipe_env(arch)
        ret['CFLAGS'] += ' -Wno-implicit-function-declaration'
        return ret


recipe = CymunkRecipe()
