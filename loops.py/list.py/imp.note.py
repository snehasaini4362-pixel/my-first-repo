thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
shallow copy= in shallow copy the refrerence of the outer objects are different and 
inner object refrerence are same .that's why when make changea into the copies list 
then also the change would 

deep copy= in deep copy the nested objects are also copied .and it dosn't change
when we make changes into the copied list.
| Feature       | Shallow Copy         | Deep Copy     |
| ------------- | -------------------- | ------------- |
| Bahar ki list | New                  | New           |
| Andar ki list | Same                 | New           |
| Nested change | Original change hota | Original safe |


