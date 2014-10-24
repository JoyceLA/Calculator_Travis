# -*- coding: utf-8 -*-
from lettuce import *
import sys
sys.path.append("../")
from Calculator import Calculator

@step(u'Given I have the number (\d+) and (\d+)')
def given_i_have_the_number1_number2(step, number1, number2):
    world.number = [int(number1),int(number2)]

@step(u'Given I have the number "([^"]*)" and "([^"]*)"')
def given_i_have_the_number1_number2(step, number1, number2):
    world.number = [float(number1),float(number2)]

@step(u'When I compute its plus')
def when_i_compute_its_factorial(step):
	cal = Calculator()
	world.number = cal.summa(world.number[0],world.number[1])
	
@step(u'When I compute its subtraction')
def when_i_compute_its_factorial(step):
	cal = Calculator()
	world.number = cal.resta(world.number[0],world.number[1])

@step(u'When I compute its multiplication')
def when_i_compute_its_factorial(step):
	cal = Calculator()
	world.number = cal.multiplica(world.number[0],world.number[1])

@step(u'When I compute its division')
def when_i_compute_its_factorial(step):
	cal = Calculator()
	world.number = cal.divide(world.number[0],world.number[1])

@step(u'Then I see the number (\d+)')
def then_i_see_the_number_1(step, expected):
    assert world.number == int(expected)

@step(u'Then I see the number "([^"]*)"')
def then_i_see_the_number_1(step, expected):
    assert float(world.number) == float(expected),"Resultado = {0} and {1}".format(world.number,expected)

