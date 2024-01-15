from tinygrad import Tensor;
N = 1024;
a = Tensor.rand(N, N)
b = Tensor.rand(N, N)
# c = (a + b).sum(axis=1)
# c.realize()
c = (a.reshape(N, 1, N) * b.T.reshape(1, N, N)).sum(axis=2);
print(c.numpy())
print(a.mean().numpy())
out = (c - (a*b))
print(out.numpy())
out2 = out.mean()
out2.realize()
out_val = out2.realize()
print(out_val.numpy())