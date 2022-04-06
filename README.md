# Projetos-Iron-Hack
# SharK Attack Dataset

The dataset includes information on shark attacks around the world, as well as data on fatality, country, year and activities practiced during the events, among other parameters.

## References

 
 - [Pandas Documentation](https://pandas.pydata.org/docs/index.html)
 - [Ocean Current Map](https://upload.wikimedia.org/wikipedia/commons/9/9b/Corrientes-oceanicas.png)

## Documentação da API

#### Retorna todos os itens

```http
  GET /api/items
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `api_key` | `string` | **Obrigatório**. A chave da sua API |

#### Retorna um item

```http
  GET /api/items/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

#### add(num1, num2)

Recebe dois números e retorna a sua soma.


## Appendix
The following questions were raised to get insights from the dataset:

Question 1: Which hemisphere has more ocurrences?
Question 2: Which hemisphere has more fatalities?
Question 3: Which activity has more fatalities?
Question 3: How Many ocurrences happens in Western Boundary Current areas?

The following information was collected from the processed data:

Northern Hemisphere has more occurrences (N-2338 S-2163);
More fatal incidents occurred in the southern hemisphere (68%);

The activity most recorded during the occurrences was surfing, but the most fatal was swimming with 24% of fatal cases, on the other hand surfing did not account for any occurrence;

Most incidents are not fatal, accounting for 75% of occurrences;

The western boundary current covers more areas in the northern hemisphere (1448), where most occurrences occur, than in the southern hemisphere (1354);

62% of occurrences occur in areas where western boundary currents are found;


