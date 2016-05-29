#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import re
import subprocess as spr

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

success_pattern = re.compile('^Failed:\s.+0$')
FORMULAS = ('vim', 'xml', 'virtualenv', 'pip')


def main():
    for formula in FORMULAS:
        cmd = ['salt-call',
               '-c', '/root/salt/states/test',
               '-linfo',
               'state.sls',
               formula]

        out = spr.check_output(cmd)
        if success_pattern.findall(out):
            logger.info("Test %s: successful.", formula)
        else:
            logger.info("Test %s: failed", formula)
            logger.info(out)


if __name__ == "__main__":
    main()
