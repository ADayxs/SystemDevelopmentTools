import torch
from torch import nn

def test_training_converges():
    torch.manual_seed(20260907)
    x = torch.linspace(-1, 1, 101).reshape(-1, 1)
    y = 3 * x - 1
    model = nn.Linear(1, 1)
    loss_fn = nn.MSELoss()
    opt = torch.optim.SGD(model.parameters(), lr=0.1)
    
    for _ in range(200):
        pred = model(x)
        loss = loss_fn(pred, y)
        opt.zero_grad()
        loss.backward()
        opt.step()
    
    model.eval()
    with torch.no_grad():
        final_loss = loss_fn(model(x), y)
    
    assert final_loss.item() < 0.001
    assert abs(model.weight.item() - 3.0) < 0.1
    assert abs(model.bias.item() + 1.0) < 0.1
