import heapq
l = [10, 20, 30, 23, 320, 48, 100, 200, 900, 5, 12, 18]
print('Before heap : ', l)
heapq.heapify(l)
print('After heap : ', l)
heapq.heappush(l, 2)
print('Push once : ', l)
heapq.heappush(l, 0)
print('Push twice : ', l)
heapq.heappop(l)
print('Pop once : ', l)
heapq.heappop(l)
print('Pop twice : ', l)
x = heapq.heappushpop(l, 6)
print('x is : ', x)
print('Push and pop : ', l)
x = heapq.heapreplace(l, 80)
print('x is : ', x)
print('Replace : ', l)
l1 = [1, 20, 34, 24, 43, 86, 100]
l2 = [100, 32,45, 65, 78, 98]
it = heapq.merge(l1, l2)
'''print(list(it))
for x in it:
    print('x : ', x)
'''
l = list(it)
lgs = heapq.nlargest(4, l)
sms = heapq.nsmallest(4, l)
print(lgs)
print(sms)