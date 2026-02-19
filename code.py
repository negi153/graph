# %%
import random

# %%
class Batch():
    def __init__(self, batch_id):
        self.batch_id = batch_id
        self.parent_batch_list = [] # [Batch('111'), Batch('222')]

    def get_parent_batch(self):
        # Get parent batch list by querying database
        # query = f"select parent_batch from <table> where batch_id = '{self.batch_id}'"
        # data = conn.execute(query)
        # self.parent_batch_list = data['parent_batch']
        
        # get this list from database
        # parent_batch_list_from_db = ['222','333']
        parent_batch_list_from_db = [str(random.randint(1,100)) for i in range(random.randint(0,2))]
        # self.parent_batch_list = [Batch(parent) for parent in parent_batch_list_from_db]


        for parent in parent_batch_list_from_db:
            obj = Batch(parent)
            obj.get_parent_batch()
            self.parent_batch_list.append(obj)



# %%
batch_id = '111'
curr_batch_obj = Batch(batch_id)

# %%
curr_batch_obj.batch_id

# %%
curr_batch_obj.parent_batch_list

# %%
curr_batch_obj.get_parent_batch()

# %%
for parent in curr_batch_obj.parent_batch_list:
    print(f"batch - {parent.batch_id}")
    print(f"parent - {parent.parent_batch_list}")
    print('-'*4)

# %%
def show_graph(curr_batch_obj):
    print("current batch id - ", curr_batch_obj.batch_id)
    print("Number of parents - ",len(curr_batch_obj.parent_batch_list))
    print("parents - ", [parent.batch_id for parent in curr_batch_obj.parent_batch_list])
    # print(curr_batch_obj.parent_batch_list)

    # if curr_batch_obj.parent_batch_list:
        
    #     print("Number of parents - ",len(curr_batch_obj.parent_batch_list))
    print('-'*10)

    for parent in curr_batch_obj.parent_batch_list:
        show_graph(parent)
    


# %%
show_graph(curr_batch_obj)

# %%



