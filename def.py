
arr = [2, 5, 7]
min = None 
for num in arr:
    if min is None or num < min:
        min = num
print(min)
class PositionalEncoding(nn.Module):

    def sum(a : int, b : int = 10):
        return a + b
    def __init__(self, d_model:int = 50, max_len : int = 5000) -> None:
        super(PositionalEncoding, self).__init__()
        pe = torch.zeros(max_len, d_model, required_grad=False)
        position = torch.arange(o, max_len, dtype = torch.float).unsqueeze(1).float()
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)
    def forward(self, length: int) -> int:
        return self.pe[:, :length]





























