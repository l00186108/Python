'''
Script: budget.py
By: NMC
Purpose: Creating a budget file
Date: 10SEPT23

'''
income = 40000
single_person_tax_allowance = 12000
taxable_at_20_percent = income - single_person_tax_allowance
taxable_at_40_percent = income - taxable_at_20_percent
percent_tax_20 = taxable_at_20_percent * .3
percent_tax_40 = taxable_at_40_percent * .5
total_tax = percent_tax_40 + percent_tax_20
print(total_tax)