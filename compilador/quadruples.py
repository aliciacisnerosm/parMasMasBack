
class Quadruple:
  def __init__(self, operator, leftOperand, rightOperand, temporal):
    self.leftOperand = leftOperand
    self.rightOperand = rightOperand
    self.operator = operator
    self.temporal = temporal
  
  def get_quadruple(self):
    return (self.operator, self.leftOperand, self.rightOperand, self.temporal)
