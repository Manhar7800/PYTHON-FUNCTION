"""

generator:it normal output as future purpose and return as a iterator

so,using yield and iterate we can use generated output
without generator.


def myfun():
  return 1
  return 2   # wrong


  def myfun():
  yield 1
  yield 2
  .
  .


"""

def  myfun():
    yield 1
    yield 2
    yield 3

    it=myfun()

    for i in it:
        print(i)


        #1 2 3 