class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
       List<String> result = new ArrayList<>();
        Set<String> availableSupplies = new HashSet<>(Arrays.asList(supplies)); // Use Set for fast lookup
        boolean addedNewRecipe;

        do {
            addedNewRecipe = false;
            for (int i = 0; i < recipes.length; i++) {
                if (!result.contains(recipes[i]) && availableSupplies.containsAll(ingredients.get(i))) {
                    result.add(recipes[i]);
                    availableSupplies.add(recipes[i]); // Add new recipe to supplies
                    addedNewRecipe = true;
                }
            }
        } while (addedNewRecipe); // Continue until no new recipes can be made

        return result;
    
    }
}
