/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: trakotoz <trakotoz@student.42antananarivo  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 18:56:01 by trakotoz          #+#    #+#             */
/*   Updated: 2026/01/22 20:17:03 by trakotoz         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	count_word(char *str, char c)
{
	size_t	count;
	size_t	i;

	count = 0;
	i = 0;
	while (str[i])
	{
		while (str[i] == c)
			i++;
		if (str[i])
			count++;
		while (str[i] && str[i] != c)
			i++;
	}
	
	return (count);
}

static char	*get_word(char *str, char c, size_t index)
{
	char	*word;
	size_t	start;
	size_t	str_len;
	size_t	word_len;
	size_t	j;

	start = index;
	str_len = ft_strlen(str);
	while (str[index] != c && index < str_len)
		index++;
	word_len = index - start;
	word = (char *) malloc(sizeof(char) * word_len);
	if (word == 0)
	{
		free(word);
		return (0);
	}
	j = 0;
	while (start < index)
	{
		word[j] = str[start];
		start++;
		j++;
	}
	return (word);
}

static void	free_all_tab(char **res, size_t index)
{
	size_t	i;

	i = 0;
	while (i < index && res[i] != 0)
		free(res[i++]);
	free(res);
}

static char	**make_split(char **ptr, char *str, char c, size_t len)
{
	size_t	i;
	size_t	j;

	i = 0;
	j = 0;
	while (str[i] && j < len)
	{
		while (str[i] == c)
			i++;
		if (str[i])
		{
			ptr[j] = get_word(str, c, i);
			if (ptr[j] == 0)
			{
				free_all_tab(ptr, i);
				return (0);
			}
			j++;
		}
		while (str[i] != c && str[i])
			i++;
	}
	return (ptr);
}

char	**ft_split(char *str, char c)
{
	char	**ptr;
	size_t	len;

	len = count_word(str, c);
	ptr = (char **) malloc(sizeof(char * ) * (len + 1));
	if (ptr == 0)
	{
		free(ptr);
		return (0);
	}
	ptr = make_split(ptr, str, c, len);

	return (ptr);
}

