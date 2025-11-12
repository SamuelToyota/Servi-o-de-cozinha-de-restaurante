<img width="1898" height="911" alt="image" src="https://github.com/user-attachments/assets/74b2482a-39e4-4be8-8b82-be742f8b5a39" />

# 🍽️ Serviço de Cozinha de Restaurante

Um sistema de gerenciamento para cozinhas profissionais.  
O objetivo é facilitar a comunicação entre os cozinheiros, permitir o registro de novos pratos, tipos de prato e ingredientes, além de indicar quais cozinheiros são responsáveis por cada prato.

---

## 📂 Estrutura do Projeto

servico_de_cozinha_de_restaurante/
├── manage.py
├── servico_de_cozinha_de_restaurante/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── menu/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ ├── admin.py
│ ├── templates/menu/
│ │ ├── base.html
│ │ ├── dish_list.html
│ │ ├── dish_detail.html
│ │ ├── cook_list.html
│ │ ├── cook_detail.html
│ │ ├── dish_type_list.html
│ │ └── ingredient_list.html
│ └── static/menu/
└── requirements.txt

yaml
Copiar código

---

## 💡 Funcionalidades

- ✅ CRUD completo de **Pratos**
- ✅ CRUD completo de **Cozinheiros**
- ✅ CRUD completo de **Tipos de Prato**
- ✅ CRUD completo de **Ingredientes**
- ✅ Relacionamentos Many-to-Many entre Cozinheiros e Pratos
- ✅ Relacionamentos Many-to-Many entre Pratos e Ingredientes
- ✅ Interface estilizada com **Bootstrap**
- ✅ Navegação simples e intuitiva

---

## 🧩 Modelos (Models)

### **DishType**
Representa a categoria de um prato (ex: “Massas”, “Sobremesas”, “Carnes”).

| Campo | Tipo | Descrição |
|--------|------|-----------|
| `name` | `CharField` | Nome do tipo de prato |

---

### **Cook**
Representa um cozinheiro.

| Campo | Tipo | Descrição |
|--------|------|-----------|
| `first_name` | `CharField` | Nome do cozinheiro |
| `last_name` | `CharField` | Sobrenome |
| `experience_years` | `PositiveIntegerField` | Anos de experiência |

---

### **Dish**
Representa um prato específico do restaurante.

| Campo | Tipo | Descrição |
|--------|------|-----------|
| `name` | `CharField` | Nome do prato |
| `description` | `TextField` | Descrição opcional |
| `dish_type` | `ForeignKey(DishType)` | Tipo de prato |
| `cooks` | `ManyToManyField(Cook)` | Cozinheiros responsáveis |
| `price` | `DecimalField` | Preço |

---

### **Ingredient**
Representa os ingredientes disponíveis.

| Campo | Tipo | Descrição |
|--------|------|-----------|
| `name` | `CharField` | Nome do ingrediente |
| `dishes` | `ManyToManyField(Dish)` | Pratos que usam esse ingrediente |

---

## 🧭 URLs principais

| Caminho | View | Descrição |
|----------|------|-----------|
| `/` | `DishListView` | Lista de pratos |
| `/dish/<id>/` | `DishDetailView` | Detalhe de um prato |
| `/dishes/create/` | `DishCreateView` | Criar novo prato |
| `/cooks/` | `CookListView` | Lista de cozinheiros |
| `/dish-types/` | `DishTypeListView` | Lista de tipos |
| `/ingredients/` | `IngredientListView` | Lista de ingredientes |

---

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/servico_de_cozinha_de_restaurante.git

   cd servico_de_cozinha_de_restaurante
