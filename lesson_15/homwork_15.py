class Diamond:
     def __init__(self, side_a, angle_a):
         self.side_a = side_a
         self.angle_a =angle_a



     def __setattr__(self, key, value):
         if key == 'side_a':
             if value <= 0:
              raise AttributeError(f'значення бути більше "0"')
         if key == 'angle_a':
              if not (0 < value < 180):
               raise AttributeError(f'значення більше "0" і не більше 180')
         if key == 'angle_b':
             raise AttributeError(f'Неможливо задати angle_b, Він автоматично обчислюється з angle_a.')

         else:
          super().__setattr__(key, value)
          super().__setattr__('angle_b',180 - value)


     def __str__(self):
        return (f'  {self.side_a}, '
        f'angle_a = {self.angle_a}°, '
        f'angle_b = {self.angle_b}°')

shape = Diamond(20, 120)
print(shape.angle_a)
print(shape.angle_b)
