import unittest

def get_check_cost(cost):
  if cost < 30000:
    bike_name= 'heroHonda'
  elif cost < 100000:
    bike_name = 'Apache'
  else:
    bike_name = 'Bullet'
  return bike_name

#push https://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@github.com/PavanKumarKunnathu/docker_practice.git


class NearestExitTests(unittest.TestCase):

  def test_row_1(self):
    self.assertEqual(get_check_cost(20000), 'heroHonda', 'The Nearest cost to row 1 is in the Herohonda!')
    
 
  def test_row_20(self):
    self.assertEqual(get_check_cost(50000), 'Apache', 'The Nearest cost to row 20 is in the Apache!')
    
  
  def test_row_40(self):
    self.assertEqual(get_check_cost(150000), 'Bullet', 'The Nearest cost to row 40 is in the bullet!')


unittest.main()
