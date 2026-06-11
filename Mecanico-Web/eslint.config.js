// @ts-check
const eslint = require("@eslint/js");
const { defineConfig } = require("eslint/config");
const tseslint = require("typescript-eslint");
const angular = require("angular-eslint");

module.exports = defineConfig([
  {
    files: ["**/*.ts"],
    extends: [
      eslint.configs.recommended,
      tseslint.configs.recommended,
      tseslint.configs.stylistic,
      angular.configs.tsRecommended,
    ],
    processor: angular.processInlineTemplates,
    rules: {
      "@angular-eslint/directive-selector": [
        "error",
        {
          type: "attribute",
          prefix: "app",
          style: "camelCase",
        },
      ],
      "@angular-eslint/component-selector": [
        "error",
        {
          type: "element",
          prefix: "app",
          style: "kebab-case",
        },
      ],

      eqeqeq: "error",  // Enforce using ""==="" instead of "=="
      curly: "error",   // Require curly braces {} for if, for,etc
      'no-eval': "error", // Disallow the use of eval()
      "no-implied-eval": "error",  // Disallow implied eval (like strings in setTimeout)

      // Disable the base ESLint rules for unused variables
      "no-unused-vars": "off",
      "no-shadow": "off",

      // Use TypeScript-specific rules instead
      "@typescript-eslint/no-unused-vars": "warn", // Warn when variables are declared but not used
      "@typescript-eslint/no-shadow": "warn",      // Warn when variable declarations shadow outer variables
      "@typescript-eslint/no-explicit-any": "warn", // Warn when using the 'any' type
      "@typescript-eslint/consistent-type-definitions": ["warn", "type"], // Prefer 'type' over 'interface'
      "@typescript-eslint/consistent-type-assertions": "warn", // Warn for inconsistent type assertions
      "@typescript-eslint/explicit-member-accessibility": [
        "error",
        { "accessibility": "no-public" } // Require explicit accessibility, but allow omitting 'public'
      ],

      "complexity": ["error", 12], // Max cyclomatic complexity per function
      "max-lines": ["warn", 300], // Max lines per file
      "one-var": ["error", "never"], // One variable declaration per statement
      "prefer-const": "error", // Prefer const over let when variables are not reassigned

      "no-var": "error", // Disallow the use of 'var'; prefer 'let' or 'const'
      "prefer-arrow-callback": "error", // Prefer using arrow functions for callbacks
      "no-useless-concat": "error", // Disallow unnecessary string concatenation

      "@angular-eslint/no-empty-lifecycle-method": "warn", // Warn on empty Angular lifecycle methods
      "@angular-eslint/prefer-output-readonly": "warn", // Prefer @Output properties to be readonly
      "@angular-eslint/prefer-standalone": "warn", // Prefer standalone components over NgModules
      "@angular-eslint/prefer-signals": "warn" // Prefer using Angular signals when appropriate
    },
  },
  {
    files: ["**/*.html"],
    extends: [
      angular.configs.templateRecommended,
      angular.configs.templateAccessibility,
    ],
    rules: {
      "@angular-eslint/template/eqeqeq": "error", // Enforce strict equality (===) in templates
      "@angular-eslint/template/use-track-by-function": "warn", // Warn if *ngFor lacks a trackBy function
      "@angular-eslint/template/cyclomatic-complexity": [
        "warn",
        { maxComplexity: 8 }  // Warn if template complexity > 8
      ], 
      "@angular-eslint/template/prefer-control-flow": "error", // Prefer *ngIf/*ngFor over complex expressions
      "@angular-eslint/template/prefer-ngsrc": "warn", // Prefer using NgSrc directive where applicable
      "@angular-eslint/template/prefer-self-closing-tags": "warn" // Prefer self-closing tags when possible
    },
  }
]);
